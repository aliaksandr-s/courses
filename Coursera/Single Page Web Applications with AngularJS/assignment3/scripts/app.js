(function () {
  'use strict'

  angular.module('NarrowItDownApp', [])
         .controller('NarrowItDownController', NarrowItDownController)
         .service('MenuSearchService', MenuSearchService)
         .directive('foundItems', FoundItemsDirective)
         .constant('ApiBasePath', "http://davids-restaurant.herokuapp.com");

  NarrowItDownController.$inject = ['MenuSearchService'];
  function NarrowItDownController(MenuSearchService) {
    var vm = this;

    vm.getMenuItems = function (searchTerm) {
      var promise = MenuSearchService.getMatchedMenuItems(searchTerm);

      promise.then(function (response) {
        vm.found = response;
      })
      .catch(function (err) {
        console.log(err)
      })
      
      vm.removeItem = function (itemIndex) {
        vm.found.splice(itemIndex, 1)
      }
    }
  }

  function FoundItemsDirective () {
    return {
      restrict: "E",
      templateUrl: "itemsList.html",
      scope: {
        foundItems: '<',
        onRemove: '&'
      },
      controller: FoundItemsDirectiveController,
      controllerAs: 'items',
      bindToController: true,
      link: FoundItemsDirectiveLink
    }
  }

  function FoundItemsDirectiveLink (scope, element, attrs, controller) {
    scope.$watch('items.foundItems', function(newVal, oldVal) {

      if (newVal instanceof Array && newVal.length === 0) {
        displayMessage()
      } else {
        removeMessage()
      }
    })

    function displayMessage () {
      var messageElement = document.querySelector(".message");
      messageElement.style.display = "block"
    }

    function removeMessage () {
      var messageElement = document.querySelector(".message");
      messageElement.style.display = "none";
    }
  }

  function FoundItemsDirectiveController () {
    var vm = this;
  }

  MenuSearchService.$inject = ['$http', 'ApiBasePath']
  function MenuSearchService($http, ApiBasePath) {
    var service = this;

    service.getMatchedMenuItems = function (searchTerm) {

      return $http.get(ApiBasePath + "/menu_items.json").then(function (result) {
        
        if (!searchTerm || searchTerm.length === 0) {
          return []
        }

        var allItems = result.data.menu_items;
        var matchedItems = []

        for (var i = 0; i < allItems.length; i++) {
          if (allItems[i].description.indexOf(searchTerm) >= 0) {
            matchedItems.push(allItems[i])
          }
        }

        return matchedItems;
      })
    }
  }
  
})();