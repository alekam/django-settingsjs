'use strict';

const settings = {{ jssettings|safe }};

const S = {
	get: function (key) { return settings[key]; },
	set: function (key, val) { return settings[key] = val; }
};

module.exports = S;
