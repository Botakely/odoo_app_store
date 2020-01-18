odoo.define('first_last_pager.Pager', function (require) {
    "use strict";

    var Pager = require('web.Pager');

    Pager.include({
        events: _.extend({}, Pager.prototype.events, {
            'click .o_pager_last': '_onLast',
            'click .o_pager_first': '_onFirst'
        }),
        _onLast: function (event) {
            event.stopPropagation();
            this.last();
        },
        _onFirst: function (event) {
            event.stopPropagation();
            this.first();
        },
        last: function () {
            var self = this;
            var size = self.state.size;
            var limit = self.state.limit;
            var current_min = self.state.current_min;
            var next = Math.floor(size / limit) - Math.floor(current_min / limit);
            if (next) {
                self._changeSelection(next);
            }
        },
        first: function () {
            var self = this;
            var limit = self.state.limit;
            var current_min = self.state.current_min;
            var previous = -Math.floor(current_min / limit);
                        console.log(this)

            if (previous) {
                this._changeSelection(previous);
            }
        }
    });

    return Pager;

});
