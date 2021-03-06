(function(){

angular.module('ui.grid')
.factory('GridRow', ['gridUtil', function(gridUtil) {

   /**
   * @ngdoc function
   * @name ui.grid.class:GridRow
   * @notes GridRow is the viewModel for one logical row on the grid.  A grid Row is not necessarily a one-to-one
   * relation to gridOptions.data.
   * @param {object} entity the array item from GridOptions.data
   * @param {number} index the current position of the row in the array
   * @param {Grid} reference to the parent grid
   */
  function GridRow(entity, index, grid) {

     /**
      *  @ngdoc object
      *  @name grid
      *  @propertyOf  ui.grid.class:GridRow
      *  @notes A reference back to the grid
      */
     this.grid = grid;

     /**
      *  @ngdoc object
      *  @name entity
      *  @propertyOf  ui.grid.class:GridRow
      *  @notes A reference to an item in gridOptions.data[]
      */
    this.entity = entity;

     /**
      *  @ngdoc object
      *  @name index
      *  @propertyOf  ui.grid.class:GridRow
      *  @notes the index of the GridRow. It should always be unique and immutable
      */
    this.index = index;


     /**
      *  @ngdoc object
      *  @name uid
      *  @propertyOf  ui.grid.class:GridRow
      *  @notes  UniqueId of row
      */
     this.uid = gridUtil.nextUid();

     /**
      *  @ngdoc object
      *  @name visible
      *  @propertyOf  ui.grid.class:GridRow
      *  @notes If true, the row will be rendered
      */
    // Default to true
    this.visible = true;
  }

  /**
   * @ngdoc function
   * @name getQualifiedColField
   * @methodOf ui.grid.class:GridRow
   * @notes returns the qualified field name as it exists on scope
   * ie: row.entity.fieldA
   * @param {GridCol} col column instance
   * @returns {string} resulting name that can be evaluated on scope
   */
  GridRow.prototype.getQualifiedColField = function(col) {
    return 'row.' + this.getEntityQualifiedColField(col);
  };

    /**
     * @ngdoc function
     * @name getEntityQualifiedColField
     * @methodOf ui.grid.class:GridRow
     * @notes returns the qualified field name minus the row path
     * ie: entity.fieldA
     * @param {GridCol} col column instance
     * @returns {string} resulting name that can be evaluated against a row
     */
  GridRow.prototype.getEntityQualifiedColField = function(col) {
    return gridUtil.preEval('entity.' + col.field);
  };

  return GridRow;
}]);

})();