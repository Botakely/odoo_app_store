odoo.define('multiple_dashboard.AddToBoardMenu', function (require) {
    "use strict";

    var AddToBoardMenu = require('board.AddToBoardMenu');
    AddToBoardMenu.include({
        init: function (parent, params) {
            this._super(parent, params);
            this.fetch_board_group_user();
        },
        fetch_board_group_user: function () {
            var self = this;
            self._rpc({
                model: 'board.group',
                method: 'fetch_user_dashboard'
            })
                .then(function (data) {
                    self.users_board_group = data;
                });
        },
        _addToBoard: function () {
            this.action.context.board_group_id = parseInt(this.$('.o_add_to_board_group_select').val());
            return this._super();
        }
    });
});
