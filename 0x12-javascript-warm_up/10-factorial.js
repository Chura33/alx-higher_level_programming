#!/usr/bin/node

const num = parseInt(process.argv[2]);
function fac (num) {
  if (num === 0 || isNaN(num) === true) {
    return (1);
  }
  if (num === 1) {
    return (1);
  } else {
    return (num * fac(num - 1));
  }
}

const res = fac(num);
console.log(res);
