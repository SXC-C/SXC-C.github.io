var amber_condload = false;
var amber_version = 'v12';
var amberv3_version ='v20210708.1';// 'v20210629.1';//'v20210608.1';

if(typeof _na === 'undefined'){
  try {
    (function(i, s, o, g, r, a, m) {
        i['NAO'] = r;
        i[r] = i[r] || function() {
            (i[r].q = i[r].q || []).push(arguments)
        }, i[r].l = 1 * new Date();
        a = s.createElement(o), m = s.getElementsByTagName(o)[0];
        a.async = 1;
        a.src = g;
        m.parentNode.insertBefore(a, m)
    })
    (window, document, 'script', 'https://www.newegg.com/gfplib.js', '_na');
  } catch (error) { }
}


try {
  (function() {
    function ul(src, a, b) {
      a = document;
      b = a.createElement('script');
      b.language = 'javascript';
      b.type = 'text/javascript';
      b.src = src;
      b.defer = true;
      a.getElementsByTagName('head')[0].appendChild(b);
    };
    ul('https://imk.neweggimages.com/webresource/scripts/amber3.lib.' + amberv3_version + '.js');
    ul('https://imk.neweggimages.com/WebResource/Scripts/amber-lib-' + amber_version + '.js');
    amber_condload = true;
  })();
} catch (e) {}