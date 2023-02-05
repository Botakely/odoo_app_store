odoo.define('web.BoardBoardUser', function (require) {
    "use strict";

    var BoardView = require('board.BoardView');
    var core = require('web.core');
    var QWeb = core.qweb;
    var Domain = require('web.Domain');
    BoardView.prototype.config.Renderer.include({
        _renderTagBoard: function (node) {
            var self = this;
            var state_context = self.state.context;
            if (state_context.hasOwnProperty('user_dashboard')) {
                node.perm_close = self.state.context.uid === self.state.context.user_dashboard;
            }
            else {
                node.perm_close = true;
            }
            return this._super(node);
        },
    });

});