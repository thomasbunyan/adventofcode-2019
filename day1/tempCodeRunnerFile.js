nst data = input.split("\n");
  data.forEach((val) => {
    totalFuel += getFuel(parseInt(val));
  });