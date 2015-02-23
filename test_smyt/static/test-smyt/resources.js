var testSmytResources = angular.module('testSmytResources', ['ngResource']);

testSmytResources.factory('ObjectsResource', function($resource) {
	'use strict';
	return $resource('/api/objects/:model/', null, {
		query: {
            method: 'GET',
            url: '/api/objects/:model/',
            isArray: false
        },
        create: {
            method: 'POST',
            url: '/api/objects/:model/new',
            isArray: false
        },
        save: {
            method: 'PATCH',
            url: '/api/objects/:model/:id/edit',
            params: {id: '@id'},
            isArray: false
        },
    });
});
