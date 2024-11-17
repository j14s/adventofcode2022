package utils

import (
	"bufio"
	"os"
)

func ReadLinesAndCount(path string) ([]string, int, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, -1, err
	}
	defer file.Close()

	var linesCount int = 0
	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
		linesCount++
	}
	return lines, linesCount, scanner.Err()
}
