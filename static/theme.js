document.addEventListener("DOMContentLoaded", function() {
    const cookieTheme = getCookie("theme"); 
    if (!cookieTheme) {
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        window.location.href = "/set_theme/dark";
      }
    }
  });
  
  function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
      "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
  }
  
  