package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
)

func downloadURL(url string, wg *sync.WaitGroup, ch chan<- string) {
	defer wg.Done()

	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprintf("Error downloading %s: %v", url, err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		ch <- fmt.Sprintf("Error reading response from %s: %v", url, err)
		return
	}

	ch <- fmt.Sprintf("Downloaded %s: %s", url, body)
}

func main() {
	var wg sync.WaitGroup
	ch := make(chan string)

	urls := []string{
		"https://brightspace.lmu.edu/d2l/home",
	}

	for _, url := range urls {
		wg.Add(1)
		go downloadURL(url, &wg, ch)
	}

	go func() {
		wg.Wait()
		close(ch)
	}()

	for message := range ch {
		fmt.Println(message)
	}
}
