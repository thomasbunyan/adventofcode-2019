const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf8");

let main = () => {
  let totalFuel = 0;
  const data = input.split("\n");
  data.forEach((val) => {
    const fuel = getFuel(parseInt(val));
    totalFuel += fuel;
    let fuelMass = fuel;
    while (fuelMass > 0) {
      let additionalFuel = getFuel(fuelMass);
      if (additionalFuel < 0) break;
      totalFuel += additionalFuel;
      fuelMass = additionalFuel;
    }
  });

  console.log(totalFuel);
};

let getFuel = (mass) => {
  return Math.floor(mass / 3) - 2;
};

main();
