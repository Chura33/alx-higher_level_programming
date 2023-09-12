#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  let newList = [];
  for (let i in list) {
    newList[i] = list[length - i - 1];
  }
  return (newList);
}
