import { readFileSync } from "fs";

type Input = {
  leftList: number[];
  rightList: number[];
};

const parseInput = (inputLocation: string) => {
  const listOne: number[] = [];
  const listTwo: number[] = [];
  const lines = readFileSync(inputLocation, "utf8").split("\n");
  for (const line of lines) {
    const [col1, col2] = line.split("   ").map(Number);
    listOne.push(col1);
    listTwo.push(col2);
  }
  return { leftList: listOne, rightList: listTwo };
};

function countAppearances(inputList: number[]) {
  const appearances = {};
  for (const currentNumber of inputList) {
    if (currentNumber in appearances) {
      appearances[currentNumber] += 1;
    } else {
      appearances[currentNumber] = 1;
    }
  }
  return appearances;
}

function searchSimilarity({ leftList, rightList }: Input) {
  let result = 0;
  const appearances = countAppearances(rightList);
  for (const currentNumber of leftList) {
    if (currentNumber in appearances) {
      result += currentNumber * appearances[currentNumber];
    }
  }
  return result;
}

const inputLocation = "day1/input.txt";
const { leftList, rightList } = parseInput(inputLocation);
const similarity = searchSimilarity({ leftList, rightList });
console.log(similarity);
