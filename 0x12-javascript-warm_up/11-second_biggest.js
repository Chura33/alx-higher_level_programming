#!/usr/bin/node

let newArr = process.argv.slice(2);

if (newArr.length <= 1) {
    console.log(0);
    return;
  }
let intArr = newArr.map(item => parseInt(item)).filter(arg => !isNaN(arg));

if (intArr.length < 2) {
    console.log(0);
    return;
  }
intArr = intArr.sort((a, b)=> {
  return (a - b);
})

console.log(intArr[intArr.length - 2]);
