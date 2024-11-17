package days

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"

	"golang.org/x/exp/maps"

	"github.com/j14s/adventofcode/2023/go/utils"
)

type GameResults struct {
	M map[string]*GameResults
	V string
}

func newGameResults() *GameResults {
	return &GameResults{M: make(map[string]*GameResults)}
}

func (c *GameResults) addIfEmpty(key string) *GameResults {
	if _, ok := c.M[key]; !ok {
		c.M[key] = newGameResults()
	}
	return c.M[key]
}

func DayTwo(part string) {

	lines, err := utils.ReadLines("inputs/2.input")
	if err != nil {
		log.Fatalf("readLines: %s", err)
	}

	var gameResults = newGameResults()

	for _, line := range lines {

		var roundCtr int = 1

		gameSplit := strings.Split(line, ":")
		gstr := regexp.MustCompile("[1-9].*")
		gameNumStr := gstr.FindStringSubmatch(gameSplit[0])
		gameRounds := gameSplit[1]

		gameNumGameResults := gameResults.addIfEmpty(gameNumStr[0])

		roundSplit := strings.Split(gameRounds, ";")
		for _, round := range roundSplit {
			roundCtrStr := strconv.Itoa(roundCtr)
			roundGameResults := gameNumGameResults.addIfEmpty(roundCtrStr)
			for _, roundTots := range strings.Split(round, ",") {
				colorCount := strings.Split(roundTots, " ")
				roundGameResults.addIfEmpty(colorCount[2]).V = colorCount[1]
				//fmt.Printf("%s : %d : %s : %s \n", gameNumStr[0], roundCtr, colorCount[2], colorCount[1])
			}
			roundCtr++
		}
	}

	var sumGoodIDs int = 0
	var cubePower int
	var cubePowerSum int = 0
	allGames := maps.Keys(gameResults.M)
	//fmt.Println("gameResults Keys:", keys)
	for _, thisGame := range allGames {
		goodGame := true
		maxR, maxG, maxB := 1, 1, 1
		//fmt.Printf("Game: %s\n", thisGame)
		allRounds := maps.Keys(gameResults.M[thisGame].M)
		for _, thisRound := range allRounds {
			//fmt.Printf("Game: %s Round: %s\n", thisGame, thisRound)
			allColors := maps.Keys(gameResults.M[thisGame].M[thisRound].M)
			for _, thisColor := range allColors {
				colorScore, err := strconv.Atoi(gameResults.M[thisGame].M[thisRound].M[thisColor].V)
				if err != nil {
					log.Fatalf("erro converting colorScore to int: %s", err)
				}
				if thisColor == "red" {
					//fmt.Printf("BAD G: %s R: %s C: %s S: %d >12\n", thisGame, thisRound, thisColor, colorScore)
					if colorScore > maxR {
						maxR = colorScore
					}
					if colorScore > 12 {
						goodGame = false
					}
				} else if thisColor == "green" {
					//fmt.Printf("BAD G: %s R: %s C: %s S: %d >12\n", thisGame, thisRound, thisColor, colorScore)
					if colorScore > maxG {
						maxG = colorScore
					}
					if colorScore > 13 {
						goodGame = false
					}
				} else if thisColor == "blue" {
					//fmt.Printf("BAD G: %s R: %s C: %s S: %d >12\n", thisGame, thisRound, thisColor, colorScore)
					if colorScore > maxB {
						maxB = colorScore
					}
					if colorScore > 14 {
						goodGame = false
					}
				}
			}
		}

		if goodGame {
			thisGameInt, err := strconv.Atoi(thisGame)
			if err != nil {
				log.Fatalf("error converting thisGame to int: %s", err)
			}
			//fmt.Printf("GOOD G: %s\n", thisGame)
			sumGoodIDs = sumGoodIDs + thisGameInt
		}

		cubePower = maxR * maxG * maxB
		cubePowerSum = cubePowerSum + cubePower
		//fmt.Printf("Game: %s CubePower: %d\n", thisGame, cubePower)
	}
	fmt.Printf("Summed Good IDs: %d\n", sumGoodIDs)
	fmt.Printf("Summed Cube Powers: %d\n", cubePowerSum)

}
