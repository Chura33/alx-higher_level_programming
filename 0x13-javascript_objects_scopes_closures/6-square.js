#!/usr/bin/node

const Square = require('./5-square');

class Square1 extends Square {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += c || 'X';
      }
      console.log(rec);
    }
  }
}
module.exports = Square1;
