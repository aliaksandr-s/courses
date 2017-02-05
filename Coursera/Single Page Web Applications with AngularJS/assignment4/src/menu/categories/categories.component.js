(function () {
  'use strict';

  angular.module('MenuApp')
  .component('categories', {
    templateUrl: 'src/menu/categories/categories.template.html',
    bindings: {
      categories: '<'
    }
  })

})();
