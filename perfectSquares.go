package main

import (
    "fmt"
    "os"
    "strconv"
)

func main() {
    max, err := strconv.Atoi(os.Args[1])

    fmt.Printf("Perfect squares up to %d:\n", max)
    for i := 1; i*i <= max; i++ {
        fmt.Println(i * i)
    }
}
