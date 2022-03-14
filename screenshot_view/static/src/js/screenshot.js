odoo.define('screenshot_view.SystrayItem', function (require) {
    "use strict";

    var SystrayMenu = require('web.SystrayMenu');
    var Widget = require('web.Widget');
    var core = require('web.core');
    var QWeb = core.qweb;
    var session  = require('web.session');
    var Context = require('web.Context');

    var SystrayItem = Widget.extend({
            events: {
                "click a[data-action]": "perform_callback",
            },

            template: 'screenshot_view.SystrayItem',

            start: function () {
                this.$dropdown = this.$(".o_screenshot_dropdown");
                return Promise.resolve(
                    this._super()
                ).then(function () {
                    return this.update();
                }.bind(this));
            },

            _onScreenshot: function (classMenu) {
                var self = this;
                var screenElement = document.querySelector(classMenu);
                var pageName = $('.breadcrumb-item.active').text() || 'screenshot';

                var filename = pageName.replace(/[^a-z0-9]/gi, '_').toLowerCase() + '.png'
                $(classMenu).addClass('highlight');
                setTimeout(
                    function () {
                        $(classMenu).removeClass('highlight');
                        html2canvas(screenElement).then(canvas => {
                            self.saveAs(canvas.toDataURL(), filename);
                    })
                        ;
                    },
                    350
                );
            },
            perform_callback: function (evt) {
                evt.preventDefault();
                var params = $(evt.target).data();
                var callback = params.action;

                if (callback && this[callback]) {
                    this[callback](params, evt);
                } else {
                    console.warn("No handler for ", callback);
                }
            },
            saveAs: function (uri, filename) {
                var link = document.createElement('a');

                if (typeof link.download === 'string') {

                    link.href = uri;
                    link.download = filename;

                    //Firefox requires the link to be in the body
                    document.body.appendChild(link);

                    //simulate click
                    link.click();

                    //remove the link when done
                    document.body.removeChild(link);

                } else {

                    window.open(uri);

                }
            },
            update: function () {
                this.$dropdown
                    .empty()
                    .append(QWeb.render('screenshot_view.SystrayItem.Submenu', {
                        manager: this,
                    }));
                return Promise.resolve();
            },
            full_screen: function () {
                this._onScreenshot('.o_web_client')
            },
            without_menubar: function () {
                this._onScreenshot('.o_action_manager')
            },
            without_control_pannel: function () {
                this._onScreenshot('.o_content')
            }
        });

    SystrayMenu.Items.unshift(SystrayItem);

    return SystrayItem;

});
