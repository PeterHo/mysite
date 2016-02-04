// select 的省市县选择脚本

// 默认配置
var settings = {
    prov: null,
    city: null,
    county: null
};
// 全局变量
var province, city, county, city_group, county_group, city_json;

// 赋值市级函数
function cityStart() {
    var prov_id = province.get(0).selectedIndex;

    if (prov_id < 0 || typeof(city_json[prov_id].c) == "undefined") {
        city_group.hide();
        county_group.hide();
        return;
    }
    city_group.show();

    // 遍历赋值市级下拉列表
    var temp_html = "";
    $.each(city_json[prov_id].c, function (i, city) {
        temp_html += "<option value='" + city.n + "'>" + city.n + "</option>";
    });
    city.html(temp_html);
    countyStart();
}

// 赋值地区（县）函数
function countyStart() {
    var prov_id = province.get(0).selectedIndex;
    var city_id = city.get(0).selectedIndex;

    if (prov_id < 0 || city_id < 0 || typeof(city_json[prov_id].c[city_id].a) == "undefined") {
        county_group.hide();
        return;
    }
    county_group.show();

    // 遍历赋值区县级下拉列表
    var temp_html = "";
    $.each(city_json[prov_id].c[city_id].a, function (i, dist) {
        temp_html += "<option value='" + dist.s + "'>" + dist.s + "</option>";
    });
    county.html(temp_html);
}

function init() {
    // 初始化省市县
    var temp_html = "";
    $.each(city_json, function (i, prov) {
        temp_html += "<option value='" + prov.p + "'>" + prov.p + "</option>";
    });
    province.html(temp_html);
    cityStart();
    countyStart();

    // 若有传入省份与市级的值，则选中
    if (settings.prov != null) {
        province.val(settings.prov);
        cityStart();
    }
    if (settings.city != null) {
        city.val(settings.city);
        countyStart();
    }
    if (settings.county != null) {
        county.val(settings.county);
    }

    province.change(function () {
        cityStart();
    });
    city.change(function () {
        countyStart();
    })
}

// url json文件url地址
// p 省份select的jquery对象
// c 城市select的jquery对象
// d 区县select的jquery对象
// cg 包裹城市市select的jquery对象,用于隐藏城市select
// dg 包裹区县select的jquery对象,用于隐藏区县select
// defaultProv 默认选中省,可为null
// defaultCity 默认选中市,可为null
// defaultCounty 默认选中区,可为null
function citySelect(url, p, c, d, cg, dg, defaultProv, defaultCity, defaultCounty) {
    settings.prov = defaultProv;
    settings.city = defaultCity;
    settings.county = defaultCounty;

    province = p;
    city = c;
    county = d;
    city_group = cg;
    county_group = dg;

    // 设置省市json数据
    $.getJSON(url, function (json) {
        city_json = json;
        init();
    });
}
