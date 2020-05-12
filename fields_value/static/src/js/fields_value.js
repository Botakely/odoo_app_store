odoo.define('fields_value.form_controller', function (require) {
    "use strict";

    var FormController = require('web.FormController');
    var session = require('web.session');

    FormController.include({
        renderSidebar: function ($node) {
            this._super($node);
            if (this.hasSidebar && session.debug) {
                this.sidebar._addToolbarActions({
                    other: [{
                        label: _t('View fields value'),
                        callback: this._onOpenFieldsValue.bind(this)
                    }]
                });
                this.sidebar.appendTo($node);
                this._updateSidebar();
            }
        },
        _onOpenFieldsValue: function () {
            var state = this.initialState;
            this.do_action({
                type: 'ir.actions.act_window',
                view_type: 'form',
                view_mode: 'form',
                res_model: 'fields.value',
                views: [[false, 'form']],
                context: {
                    default_res_id: state.res_id,
                    default_model: state.model,
                    from_fields_value: true
                },
                target: 'new'
            });
        }
    })
});
