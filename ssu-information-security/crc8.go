package main

import (
    "fmt"
    "os"
    "log"
)

func main() {
	// Polynom
	var poly byte = 0xD5
    // Open file for reading
    file, err := os.Open("input.txt")
    if err != nil {
        log.Fatal(err)
    }

    for true {
        b := make([]byte, 1)
        _, err := file.Read(b)
        if err != nil {
        	break
        }
        fmt.Printf("Read byte: %d \n", int(b[0]))
    }
}