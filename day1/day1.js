const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf8");

let main = () => {
  let totalFuel = 0;
  const data = input.split("\n");
  data.forEach((val) => {
    totalFuel += getFuel(parseInt(val));
  });
  console.log(totalFuel);
};

let getFuel = (mass) => {
  return Math.floor(mass / 3) - 2;
};

main();
