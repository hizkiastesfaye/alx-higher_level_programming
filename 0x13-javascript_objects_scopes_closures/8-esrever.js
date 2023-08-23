#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduce((reversed, current) => [current, ...reversed], []);
};
