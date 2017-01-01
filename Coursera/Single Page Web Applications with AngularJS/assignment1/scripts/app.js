(function () {
  'use strict';

  angular.module('LunchCheck', [])
  .controller('LunchCheckController', LunchCheckController);

  LunchCheckController.$inject = ['$scope']

  function LunchCheckController ($scope) {
    
    $scope.check = function () {

      var items = countLunchItems($scope.lunch);

      if (items === 0) {

        $scope.message = 'Please enter data first';
        $scope.color = 'text-danger';
        $scope.border = 'border-red';

      } else if (items <= 3) {

        $scope.message = 'Enjoy!';
        $scope.color = 'text-success';
        $scope.border = 'border-green'

      } else {

        $scope.message = 'Too much!';
        $scope.color = 'text-success';
        $scope.border = 'border-green'
        
      }
    }

    function countLunchItems (lunch) {
      if (!lunch) return 0;
      return lunch.split(',').length;
    }
  }

})();