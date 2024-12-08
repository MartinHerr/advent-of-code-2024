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

const totalDistance = ({ leftList, rightList }: Input) => {
  leftList.sort();
  rightList.sort();
  let distance = 0;
  for (let i = 0; i < leftList.length; i++) {
    distance += Math.abs(rightList[i] - leftList[i]);
  }
  return distance;
};

const inputLocation = "day1/input.txt";
const { leftList, rightList } = parseInput(inputLocation);
const distance = totalDistance({ leftList, rightList });
// console.log(leftList);
// console.log(rightList);
console.log(distance);
