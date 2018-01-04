
const settings = {{ jssettings|safe }}

const S = {
    get: function(key, default_) {
        if (settings[key] === undefined)
            return default_
        else
            return settings[key]
    },
    set: function(key, val) {
        settings[key] = val
    },
    static: function(key) {
        if (key)
            return this.get('STATIC_URL') + key
        else
            return this.get('STATIC_URL')
    }
};

module.exports = S
