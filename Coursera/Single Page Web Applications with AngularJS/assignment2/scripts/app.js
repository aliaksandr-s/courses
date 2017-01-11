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

    toBuy.items = ShoppingListCheckOffService.toBuy;

    toBuy.moveToBought = ShoppingListCheckOffService.moveToBought;
  }

  AlreadyBoughtController.$inject = ['ShoppingListCheckOffService'];
  function AlreadyBoughtController(ShoppingListCheckOffService) {
    var bought = this;

    bought.items = ShoppingListCheckOffService.bought;
  }

  //services
  function ShoppingListCheckOffService() {
    var service = this;

    service.toBuy = [
      { name: "cookies", quantity: 10 },
      { name: "bread", quantity: 1 },
      { name: "apples", quantity: 10 },
      { name: "bananas", quantity: 5 },
      { name: "tomatoes", quantity: 2 }
    ];

    service.bought = [];

    service.moveToBought = function (itemIndex) {
      var removed = service.toBuy.splice(itemIndex, 1)[0];
      service.bought.push(removed)
    }

  }

})();