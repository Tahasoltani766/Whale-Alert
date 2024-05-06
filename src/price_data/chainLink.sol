// SPDX-License-Identifier: MIT
pragma solidity ^0.8.25;


import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract ChainLinkPrice {
  AggregatorV3Interface internal priceFeed;

  function getLatestPrice(address aggAddr) public view returns (int) {
    (,int256 price,,,) = AggregatorV3Interface(aggAddr).latestRoundData();
    return price;
}
}
