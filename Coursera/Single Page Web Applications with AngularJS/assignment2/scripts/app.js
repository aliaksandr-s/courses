(function () {
  'use strict';

  angular.module('ShoppingListCheckOff', [])
    .controller('ToBuyController', ToBuyController)
    .controller('AlreadyBoughtController', AlreadyBoughtController)
    .service('ShoppingListCheckOffService', ShoppingListCheckOffService)
 
  //controllers
  ToBuyController.$inject = ['ShoppingListCheckOffService'];
  function ToBuyController(ShoppingListCheckOffService) {
    var toBuy = this;

    toBuy.items = ShoppingListCheckOffService.getToBuy();

    toBuy.moveToBought = ShoppingListCheckOffService.moveToBought;
  }

  AlreadyBoughtController.$inject = ['ShoppingListCheckOffService'];
  function AlreadyBoughtController(ShoppingListCheckOffService) {
    var bought = this;

    bought.items = ShoppingListCheckOffService.getBought();
  }

  //services
  function ShoppingListCheckOffService() {
    var service = this;

    var toBuy = [
      { name: "cookies", quantity: 10 },
      { name: "bread", quantity: 1 },
      { name: "apples", quantity: 10 },
      { name: "bananas", quantity: 5 },
      { name: "tomatoes", quantity: 2 }
    ];

    var bought = [];

    service.getToBuy = function () {
      return toBuy;
    }

    service.getBought = function () {
      return bought;
    }

    service.moveToBought = function (itemIndex) {
      var removed = toBuy.splice(itemIndex, 1)[0];
      bought.push(removed)
    }

  }

})();