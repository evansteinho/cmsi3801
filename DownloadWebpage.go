package main

import (
    "fmt"
    "io"
    "net/http"
    "os"
)

func main() {
    url := os.Args[1]

    resp, err := http.Get(url)
    defer resp.Body.Close()

    bodyBytes, err := io.ReadAll(resp.Body)

    bodyString := string(bodyBytes)
    fmt.Println(bodyString)
}
