var testSmytDirectives = angular.module('testSmytDirectives', []);

testSmytDirectives.directive('editableField', function($window){
	'use strict';
	return {
		restrict: 'EA',
		scope: {
			field: '=',
			type: '=',
			editable: '=',
			model: '=',
			object: '='
		},
		link: function($scope, $element){
			$scope.isEdit = false;
			if($scope.editable){
				$scope.edit = function(){
					$scope.isEdit = true;
					$element.find('input').one('blur', function(){
						$scope.isEdit = false;
						$scope.object.$save({model: $scope.model});
					});
				};
				
			}
		},
		templateUrl: $window.STATIC_URL + 'test-smyt/tmpl/editable-field.html'
	};
});