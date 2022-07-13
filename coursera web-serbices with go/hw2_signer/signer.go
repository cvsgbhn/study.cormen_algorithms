package main

import (
	"strconv"
)

func ExecutePipeline(jobs ...job) {
	in := make(chan interface{})
	out := make(chan interface{})

	for i := range jobs {
		go jobs[i](in, out)
	}
}

func SingleHash(in, out chan interface{}) {
	data := <-in
	first := DataSignerCrc32(data.(string))
	second := DataSignerCrc32(DataSignerMd5(data.(string)))
	out <- first + "~" + second
}

func MultiHash(in, out chan interface{}) {
	var newData string
	data := <-in

	for i := 0; i < 6; i++ {
		j := strconv.Itoa(i)
		newData += DataSignerCrc32(j + data.(string))
	}

	out <- newData
}

func CombineResults(in, out chan interface{}) {
	var res string
	//last := <-in

	select {
	case last := <-in:
		res += "-" + last.(string)
	}

	out <- res
}
