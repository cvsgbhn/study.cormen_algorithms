package main

import (
	"io"
	"os"
	"sort"
	"strconv"
)

type File struct {
	Name        string
	IsDir       bool
	Prefix      string
	Size        string
	FilesInside []File
}

const (
	prefix     = "├───"
	lastPrefix = "└───"
)

func makeArr(files []os.DirEntry, tabs []string) ([]File, []string) {
	fileNamesMap := make(map[string]bool, len(files))
	fileSizesMap := make(map[string]string, len(files))
	fileNames := make([]string, len(files))
	finalFiles := make([]File, len(files))

	for i, v := range files {
		fileNamesMap[v.Name()] = v.IsDir()
		info, _ := v.Info()
		s := int(info.Size())
		if s == 0 {
			fileSizesMap[v.Name()] = " (empty)"
		} else {
			fileSizesMap[v.Name()] = " (" + strconv.Itoa(s) + "b)"
		}
		fileNames[i] = v.Name()
	}

	sort.Strings(fileNames)

	var allTabs string
	for _, v := range tabs {
		allTabs += v
	}

	for i, v := range fileNames {

		finalFiles[i] = File{
			Name:   v,
			IsDir:  fileNamesMap[v],
			Prefix: allTabs + prefix,
			Size:   fileSizesMap[v],
		}
	}

	if len(finalFiles) > 0 {
		finalFiles[len(fileNames)-1].Prefix = allTabs + lastPrefix
	}

	return finalFiles, tabs
}

func makeTree(path string, tabs []string, printFiles bool) []File {
	file, err := os.Open(path)
	if err != nil {
		return nil
	}

	files, err := file.ReadDir(0)
	if err != nil {
		return nil
	}

	if !printFiles {
		var dirs []os.DirEntry
		for _, f := range files {
			if f.IsDir() {
				dirs = append(dirs, f)
			}
		}
		files = dirs
	}

	level, tabs := makeArr(files, tabs)

	for i, v := range level {
		var newTabs []string
		if i != len(level)-1 {
			newTabs = append(tabs, "│", "\t")
		} else {
			newTabs = append(tabs, "\t")
		}
		if v.IsDir {
			level[i].FilesInside = makeTree(path+"/"+v.Name, newTabs, printFiles)
		}
	}

	return level
}

func printTree(tree []File, out io.Writer) {
	for _, v := range tree {
		if !v.IsDir {
			out.Write([]byte(v.Prefix + v.Name + v.Size + "\n"))
		}
		if v.IsDir {
			out.Write([]byte(v.Prefix + v.Name + "\n"))
			printTree(v.FilesInside, out)
		}
	}
}

func dirTree(out io.Writer, path string, printFiles bool) error {
	tabs := make([]string, 0)
	tree := makeTree(path, tabs, printFiles)
	printTree(tree, out)

	return nil
}

func main() {
	out := os.Stdout
	if !(len(os.Args) == 2 || len(os.Args) == 3) {
		panic("usage go run main.go . [-f]")
	}
	path := os.Args[1]
	printFiles := len(os.Args) == 3 && os.Args[2] == "-f"
	err := dirTree(out, path, printFiles)
	if err != nil {
		panic(err.Error())
	}
}
