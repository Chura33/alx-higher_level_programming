#!/usr/bin/node

exports.esrever = function (list) {
  const length = list.length;
  const newList = [];
  for (const i in list) {
    newList[i] = list[length - i - 1];
  }
  return (newList);
};
