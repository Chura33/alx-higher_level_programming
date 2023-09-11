#!/usr/bin/node

const newArr = process.argv.slice(2);

if (newArr.length <= 1) {
  console.log(0);
} else {
  let intArr = newArr.map(item => parseInt(item)).filter(arg => !isNaN(arg));

  if (intArr.length < 2) {
    console.log(0);
  } else {
    intArr = intArr.sort((a, b) => {
      return (a - b);
    });

    console.log(intArr[intArr.length - 2]);
  }
}
