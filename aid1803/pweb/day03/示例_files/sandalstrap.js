if("undefined"==typeof jQuery)throw new Error("Bootstrap's JavaScript requires jQuery");+function(t){"use strict";var e=t.fn.jquery.split(" ")[0].split(".");if(e[0]<2&&e[1]<9||1==e[0]&&9==e[1]&&e[2]<1||e[0]>3)throw new Error("Bootstrap's JavaScript requires jQuery version 1.9.1 or higher, but lower than version 4")}(jQuery),+function(t){"use strict";function e(e){var r=e.attr("data-target");r||(r=e.attr("href"),r=r&&/#[A-Za-z]/.test(r)&&r.replace(/.*(?=#[^\s]*$)/,""));var n=r&&t(r);return n&&n.length?n:e.parent()}function r(r){r&&3===r.which||r&&r.target.parentNode.className.indexOf&&r.target.parentNode.className.indexOf("disabled")>-1||(t(o).remove(),t(a).each(function(){var n=t(this),o=e(n),a={relatedTarget:this};o.hasClass("open")&&(r&&"click"==r.type&&/input|textarea/i.test(r.target.tagName)&&t.contains(o[0],r.target)||(o.trigger(r=t.Event("hide.bs.dropdown",a)),r.isDefaultPrevented()||(n.attr("aria-expanded","false"),o.removeClass("open").trigger(t.Event("hidden.bs.dropdown",a)))))}))}function n(e){return this.each(function(){var r=t(this),n=r.data("bs.dropdown");n||r.data("bs.dropdown",n=new i(this)),"string"==typeof e&&n[e].call(r)})}var o=".dropdown-backdrop",a='[data-toggle="dropdown"]',i=function(e){t(e).on("click.bs.dropdown",this.toggle)};i.VERSION="3.3.7",i.prototype.toggle=function(n){var o=t(this);if(!o.is(".disabled, :disabled")){var a=e(o),i=a.hasClass("open");if(r(),!i){"ontouchstart"in document.documentElement&&!a.closest(".navbar-nav").length&&t(document.createElement("div")).addClass("dropdown-backdrop").insertAfter(t(this)).on("click",r);var d={relatedTarget:this};if(a.trigger(n=t.Event("show.bs.dropdown",d)),n.isDefaultPrevented())return;o.trigger("focus").attr("aria-expanded","true"),a.toggleClass("open").trigger(t.Event("shown.bs.dropdown",d))}return!1}},i.prototype.keydown=function(r){if(/(38|40|27|32)/.test(r.which)&&!/input|textarea/i.test(r.target.tagName)){var n=t(this);if(r.preventDefault(),r.stopPropagation(),!n.is(".disabled, :disabled")){var o=e(n),i=o.hasClass("open");if(!i&&27!=r.which||i&&27==r.which)return 27==r.which&&o.find(a).trigger("focus"),n.trigger("click");var d=" li:not(.disabled):visible a",s=o.find(".dropdown-menu"+d);if(s.length){var c=s.index(r.target);38==r.which&&c>0&&c--,40==r.which&&c<s.length-1&&c++,~c||(c=0),s.eq(c).trigger("focus")}}}};var d=t.fn.dropdown;t.fn.dropdown=n,t.fn.dropdown.Constructor=i,t.fn.dropdown.noConflict=function(){return t.fn.dropdown=d,this},t(document).on("click",r).on("click",".dropdown form",function(t){t.stopPropagation()}).on("click",a,i.prototype.toggle).on("keydown",a,i.prototype.keydown).on("keydown",".dropdown-menu",i.prototype.keydown)}(jQuery);
//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImJsb2dfd3JpdGUuanMiXSwibmFtZXMiOlsialF1ZXJ5IiwiRXJyb3IiLCIkIiwidmVyc2lvbiIsImZuIiwianF1ZXJ5Iiwic3BsaXQiLCJnZXRQYXJlbnQiLCIkdGhpcyIsInNlbGVjdG9yIiwiYXR0ciIsInRlc3QiLCJyZXBsYWNlIiwiJHBhcmVudCIsImxlbmd0aCIsInBhcmVudCIsImNsZWFyTWVudXMiLCJlIiwid2hpY2giLCJ0YXJnZXQiLCJwYXJlbnROb2RlIiwiY2xhc3NOYW1lIiwiaW5kZXhPZiIsImJhY2tkcm9wIiwicmVtb3ZlIiwidG9nZ2xlIiwiZWFjaCIsInRoaXMiLCJyZWxhdGVkVGFyZ2V0IiwiaGFzQ2xhc3MiLCJ0eXBlIiwidGFnTmFtZSIsImNvbnRhaW5zIiwidHJpZ2dlciIsIkV2ZW50IiwiaXNEZWZhdWx0UHJldmVudGVkIiwicmVtb3ZlQ2xhc3MiLCJQbHVnaW4iLCJvcHRpb24iLCJkYXRhIiwiRHJvcGRvd24iLCJjYWxsIiwiZWxlbWVudCIsIm9uIiwiVkVSU0lPTiIsInByb3RvdHlwZSIsImlzIiwiaXNBY3RpdmUiLCJkb2N1bWVudCIsImRvY3VtZW50RWxlbWVudCIsImNsb3Nlc3QiLCJjcmVhdGVFbGVtZW50IiwiYWRkQ2xhc3MiLCJpbnNlcnRBZnRlciIsInRvZ2dsZUNsYXNzIiwia2V5ZG93biIsInByZXZlbnREZWZhdWx0Iiwic3RvcFByb3BhZ2F0aW9uIiwiZmluZCIsImRlc2MiLCIkaXRlbXMiLCJpbmRleCIsImVxIiwib2xkIiwiZHJvcGRvd24iLCJDb25zdHJ1Y3RvciIsIm5vQ29uZmxpY3QiXSwibWFwcGluZ3MiOiJBQVVBLEdBQXNCLG1CQUFYQSxRQUNULEtBQU0sSUFBSUMsT0FBTSwyQ0FFakIsU0FBVUMsR0FDVCxZQUNBLElBQUlDLEdBQVVELEVBQUVFLEdBQUdDLE9BQU9DLE1BQU0sS0FBSyxHQUFHQSxNQUFNLElBQzlDLElBQUtILEVBQVEsR0FBSyxHQUFLQSxFQUFRLEdBQUssR0FBcUIsR0FBZEEsRUFB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QUF1QixJQUFYOUIsRUFBRUMsT0FBZTZCLEdBQXVCLElBQVg5QixFQUFFQyxNQUU5QyxNQURlLEtBQVhELEVBQUVDLE9BQWFMLEVBQVE2QyxLQUFLakMsR0FBUVEsUUFBUSxTQUN6Q3pCLEVBQU15QixRQUFRLFFBR3ZCLElBQUkwQixHQUFPLCtCQUNQQyxFQUFTL0MsRUFBUTZDLEtBQUssaUJBQW1CQyxFQUU3QyxJQUFLQyxFQUFPOUMsT0FBWixDQUVBLEdBQUkrQyxHQUFRRCxFQUFPQyxNQUFNNUMsRUFBRUUsT0FFWixLQUFYRixFQUFFQyxPQUFlMkMsRUFBUSxHQUFtQkEsSUFDakMsSUFBWDVDLEVBQUVDLE9BQWUyQyxFQUFRRCxFQUFPOUMsT0FBUyxHQUFHK0MsS0FDMUNBLElBQTBDQSxFQUFRLEdBRXhERCxFQUFPRSxHQUFHRCxHQUFPNUIsUUFBUSxZQWlCM0IsSUFBSThCLEdBQU03RCxFQUFFRSxHQUFHNEQsUUFFZjlELEdBQUVFLEdBQUc0RCxTQUF1QjNCLEVBQzVCbkMsRUFBRUUsR0FBRzRELFNBQVNDLFlBQWN6QixFQU01QnRDLEVBQUVFLEdBQUc0RCxTQUFTRSxXQUFhLFdBRXpCLE1BREFoRSxHQUFFRSxHQUFHNEQsU0FBV0QsRUFDVHBDLE1BT1R6QixFQUFFOEMsVUFDQ0wsR0FBRyxRQUFTM0IsR0FDWjJCLEdBQUcsUUFBUyxpQkFBa0IsU0FBVTFCLEdBQUtBLEVBQUV3QyxvQkFDL0NkLEdBQUcsUUFBU2xCLEVBQVFlLEVBQVNLLFVBQVVwQixRQUN2Q2tCLEdBQUcsVUFBV2xCLEVBQVFlLEVBQVNLLFVBQVVVLFNBQ3pDWixHQUFHLFVBQVcsaUJBQWtCSCxFQUFTSyxVQUFVVSxVQUV0RHZEIiwiZmlsZSI6InNhbmRhbHN0cmFwLm1pbi5qcyIsInNvdXJjZXNDb250ZW50IjpbIi8qIVxuICogQm9vdHN0cmFwIHYzLjMuNyAoaHR0cDovL2dldGJvb3RzdHJhcC5jb20pXG4gKiBDb3B5cmlnaHQgMjAxMS0yMDE4IFR3aXR0ZXIsIEluYy5cbiAqIExpY2Vuc2VkIHVuZGVyIE1JVCAoaHR0cHM6Ly9naXRodWIuY29tL3R3YnMvYm9vdHN0cmFwL2Jsb2IvbWFzdGVyL0xJQ0VOU0UpXG4gKi9cblxuLyohXG4gKiBHZW5lcmF0ZWQgdXNpbmcgdGhlIEJvb3RzdHJhcCBDdXN0b21pemVyICg8bm9uZT4pXG4gKiBDb25maWcgc2F2ZWQgdG8gY29uZmlnLmpzb24gYW5kIDxub25lPlxuICovXG5pZiAodHlwZW9mIGpRdWVyeSA9PT0gJ3VuZGVmaW5lZCcpIHtcbiAgdGhyb3cgbmV3IEVycm9yKCdCb290c3RyYXBcXCdzIEphdmFTY3JpcHQgcmVxdWlyZXMgalF1ZXJ5Jylcbn1cbitmdW5jdGlvbiAoJCkge1xuICAndXNlIHN0cmljdCc7XG4gIHZhciB2ZXJzaW9uID0gJC5mbi5qcXVlcnkuc3BsaXQoJyAnKVswXS5zcGxpdCgnLicpXG4gIGlmICgodmVyc2lvblswXSA8IDIgJiYgdmVyc2lvblsxXSA8IDkpIHx8ICh2ZXJzaW9uWzBdID09IDEgJiYgdmVyc2lvblsxXSA9PSA5ICYmIHZlcnNpb25bMl0gPCAxKSB8fCAodmVyc2lvblswXSA+IDMpKSB7XG4gICAgdGhyb3cgbmV3IEVycm9yKCdCb290c3RyYXBcXCdzIEphdmFTY3JpcHQgcmVxdWlyZXMgalF1ZXJ5IHZlcnNpb24gMS45LjEgb3IgaGlnaGVyLCBidXQgbG93ZXIgdGhhbiB2ZXJzaW9uIDQnKVxuICB9XG59KGpRdWVyeSk7XG5cbi8qID09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PVxuICogQm9vdHN0cmFwOiBkcm9wZG93bi5qcyB2My4zLjdcbiAqIGh0dHA6Ly9nZXRib290c3RyYXAuY29tL2phdmFzY3JpcHQvI2Ryb3Bkb3duc1xuICogPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09XG4gKiBDb3B5cmlnaHQgMjAxMS0yMDE2IFR3aXR0ZXIsIEluYy5cbiAqIExpY2Vuc2VkIHVuZGVyIE1JVCAoaHR0cHM6Ly9naXRodWIuY29tL3R3YnMvYm9vdHN0cmFwL2Jsb2IvbWFzdGVyL0xJQ0VOU0UpXG4gKiA9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0gKi9cblxuXG4rZnVuY3Rpb24gKCQpIHtcbiAgJ3VzZSBzdHJpY3QnO1xuXG4gIC8vIERST1BET1dOIENMQVNTIERFRklOSVRJT05cbiAgLy8gPT09PT09PT09PT09PT09PT09PT09PT09PVxuXG4gIHZhciBiYWNrZHJvcCA9ICcuZHJvcGRvd24tYmFja2Ryb3AnXG4gIHZhciB0b2dnbGUgICA9ICdbZGF0YS10b2dnbGU9XCJkcm9wZG93blwiXSdcbiAgdmFyIERyb3Bkb3duID0gZnVuY3Rpb24gKGVsZW1lbnQpIHtcbiAgICAkKGVsZW1lbnQpLm9uKCdjbGljay5icy5kcm9wZG93bicsIHRoaXMudG9nZ2xlKVxuICB9XG5cbiAgRHJvcGRvd24uVkVSU0lPTiA9ICczLjMuNydcblxuICBmdW5jdGlvbiBnZXRQYXJlbnQoJHRoaXMpIHtcbiAgICB2YXIgc2VsZWN0b3IgPSAkdGhpcy5hdHRyKCdkYXRhLXRhcmdldCcpXG5cbiAgICBpZiAoIXNlbGVjdG9yKSB7XG4gICAgICBzZWxlY3RvciA9ICR0aGlzLmF0dHIoJ2hyZWYnKVxuICAgICAgc2VsZWN0b3IgPSBzZWxlY3RvciAmJiAvI1tBLVphLXpdLy50ZXN0KHNlbGVjdG9yKSAmJiBzZWxlY3Rvci5yZXBsYWNlKC8uKig/PSNbXlxcc10qJCkvLCAnJykgLy8gc3RyaXAgZm9yIGllN1xuICAgIH1cblxuICAgIHZhciAkcGFyZW50ID0gc2VsZWN0b3IgJiYgJChzZWxlY3RvcilcblxuICAgIHJldHVybiAkcGFyZW50ICYmICRwYXJlbnQubGVuZ3RoID8gJHBhcmVudCA6ICR0aGlzLnBhcmVudCgpXG4gIH1cblxuICBmdW5jdGlvbiBjbGVhck1lbnVzKGUpIHtcbiAgICBpZiAoZSAmJiBlLndoaWNoID09PSAzKSByZXR1cm5cbiAgICBpZiAoZSAmJiBlLnRhcmdldC5wYXJlbnROb2RlLmNsYXNzTmFtZS5pbmRleE9mICYmIGUudGFyZ2V0LnBhcmVudE5vZGUuY2xhc3NOYW1lLmluZGV4T2YoJ2Rpc2FibGVkJykgPiAtMSkgcmV0dXJuXG4gICAgJChiYWNrZHJvcCkucmVtb3ZlKClcbiAgICAkKHRvZ2dsZSkuZWFjaChmdW5jdGlvbiAoKSB7XG4gICAgICB2YXIgJHRoaXMgICAgICAgICA9ICQodGhpcylcbiAgICAgIHZhciAkcGFyZW50ICAgICAgID0gZ2V0UGFyZW50KCR0aGlzKVxuICAgICAgdmFyIHJlbGF0ZWRUYXJnZXQgPSB7IHJlbGF0ZWRUYXJnZXQ6IHRoaXMgfVxuXG4gICAgICBpZiAoISRwYXJlbnQuaGFzQ2xhc3MoJ29wZW4nKSkgcmV0dXJuXG5cbiAgICAgIGlmIChlICYmIGUudHlwZSA9PSAnY2xpY2snICYmIC9pbnB1dHx0ZXh0YXJlYS9pLnRlc3QoZS50YXJnZXQudGFnTmFtZSkgJiYgJC5jb250YWlucygkcGFyZW50WzBdLCBlLnRhcmdldCkpIHJldHVyblxuXG4gICAgICAkcGFyZW50LnRyaWdnZXIoZSA9ICQuRXZlbnQoJ2hpZGUuYnMuZHJvcGRvd24nLCByZWxhdGVkVGFyZ2V0KSlcblxuICAgICAgaWYgKGUuaXNEZWZhdWx0UHJldmVudGVkKCkpIHJldHVyblxuXG4gICAgICAkdGhpcy5hdHRyKCdhcmlhLWV4cGFuZGVkJywgJ2ZhbHNlJylcbiAgICAgICRwYXJlbnQucmVtb3ZlQ2xhc3MoJ29wZW4nKS50cmlnZ2VyKCQuRXZlbnQoJ2hpZGRlbi5icy5kcm9wZG93bicsIHJlbGF0ZWRUYXJnZXQpKVxuICAgIH0pXG4gIH1cblxuICBEcm9wZG93bi5wcm90b3R5cGUudG9nZ2xlID0gZnVuY3Rpb24gKGUpIHtcbiAgICB2YXIgJHRoaXMgPSAkKHRoaXMpXG5cbiAgICBpZiAoJHRoaXMuaXMoJy5kaXNhYmxlZCwgOmRpc2FibGVkJykpIHJldHVyblxuXG4gICAgdmFyICRwYXJlbnQgID0gZ2V0UGFyZW50KCR0aGlzKVxuICAgIHZhciBpc0FjdGl2ZSA9ICRwYXJlbnQuaGFzQ2xhc3MoJ29wZW4nKVxuXG4gICAgY2xlYXJNZW51cygpXG5cbiAgICBpZiAoIWlzQWN0aXZlKSB7XG4gICAgICBpZiAoJ29udG91Y2hzdGFydCcgaW4gZG9jdW1lbnQuZG9jdW1lbnRFbGVtZW50ICYmICEkcGFyZW50LmNsb3Nlc3QoJy5uYXZiYXItbmF2JykubGVuZ3RoKSB7XG4gICAgICAgIC8vIGlmIG1vYmlsZSB3ZSB1c2UgYSBiYWNrZHJvcCBiZWNhdXNlIGNsaWNrIGV2ZW50cyBkb24ndCBkZWxlZ2F0ZVxuICAgICAgICAkKGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2RpdicpKVxuICAgICAgICAgIC5hZGRDbGFzcygnZHJvcGRvd24tYmFja2Ryb3AnKVxuICAgICAgICAgIC5pbnNlcnRBZnRlcigkKHRoaXMpKVxuICAgICAgICAgIC5vbignY2xpY2snLCBjbGVhck1lbnVzKVxuICAgICAgfVxuXG4gICAgICB2YXIgcmVsYXRlZFRhcmdldCA9IHsgcmVsYXRlZFRhcmdldDogdGhpcyB9XG4gICAgICAkcGFyZW50LnRyaWdnZXIoZSA9ICQuRXZlbnQoJ3Nob3cuYnMuZHJvcGRvd24nLCByZWxhdGVkVGFyZ2V0KSlcblxuICAgICAgaWYgKGUuaXNEZWZhdWx0UHJldmVudGVkKCkpIHJldHVyblxuXG4gICAgICAkdGhpc1xuICAgICAgICAudHJpZ2dlcignZm9jdXMnKVxuICAgICAgICAuYXR0cignYXJpYS1leHBhbmRlZCcsICd0cnVlJylcblxuICAgICAgJHBhcmVudFxuICAgICAgICAudG9nZ2xlQ2xhc3MoJ29wZW4nKVxuICAgICAgICAudHJpZ2dlcigkLkV2ZW50KCdzaG93bi5icy5kcm9wZG93bicsIHJlbGF0ZWRUYXJnZXQpKVxuICAgIH1cblxuICAgIHJldHVybiBmYWxzZVxuICB9XG5cbiAgRHJvcGRvd24ucHJvdG90eXBlLmtleWRvd24gPSBmdW5jdGlvbiAoZSkge1xuICAgIGlmICghLygzOHw0MHwyN3wzMikvLnRlc3QoZS53aGljaCkgfHwgL2lucHV0fHRleHRhcmVhL2kudGVzdChlLnRhcmdldC50YWdOYW1lKSkgcmV0dXJuXG5cbiAgICB2YXIgJHRoaXMgPSAkKHRoaXMpXG5cbiAgICBlLnByZXZlbnREZWZhdWx0KClcbiAgICBlLnN0b3BQcm9wYWdhdGlvbigpXG5cbiAgICBpZiAoJHRoaXMuaXMoJy5kaXNhYmxlZCwgOmRpc2FibGVkJykpIHJldHVyblxuXG4gICAgdmFyICRwYXJlbnQgID0gZ2V0UGFyZW50KCR0aGlzKVxuICAgIHZhciBpc0FjdGl2ZSA9ICRwYXJlbnQuaGFzQ2xhc3MoJ29wZW4nKVxuXG4gICAgaWYgKCFpc0FjdGl2ZSAmJiBlLndoaWNoICE9IDI3IHx8IGlzQWN0aXZlICYmIGUud2hpY2ggPT0gMjcpIHtcbiAgICAgIGlmIChlLndoaWNoID09IDI3KSAkcGFyZW50LmZpbmQodG9nZ2xlKS50cmlnZ2VyKCdmb2N1cycpXG4gICAgICByZXR1cm4gJHRoaXMudHJpZ2dlcignY2xpY2snKVxuICAgIH1cblxuICAgIHZhciBkZXNjID0gJyBsaTpub3QoLmRpc2FibGVkKTp2aXNpYmxlIGEnXG4gICAgdmFyICRpdGVtcyA9ICRwYXJlbnQuZmluZCgnLmRyb3Bkb3duLW1lbnUnICsgZGVzYylcblxuICAgIGlmICghJGl0ZW1zLmxlbmd0aCkgcmV0dXJuXG5cbiAgICB2YXIgaW5kZXggPSAkaXRlbXMuaW5kZXgoZS50YXJnZXQpXG5cbiAgICBpZiAoZS53aGljaCA9PSAzOCAmJiBpbmRleCA+IDApICAgICAgICAgICAgICAgICBpbmRleC0tICAgICAgICAgLy8gdXBcbiAgICBpZiAoZS53aGljaCA9PSA0MCAmJiBpbmRleCA8ICRpdGVtcy5sZW5ndGggLSAxKSBpbmRleCsrICAgICAgICAgLy8gZG93blxuICAgIGlmICghfmluZGV4KSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGluZGV4ID0gMFxuXG4gICAgJGl0ZW1zLmVxKGluZGV4KS50cmlnZ2VyKCdmb2N1cycpXG4gIH1cblxuXG4gIC8vIERST1BET1dOIFBMVUdJTiBERUZJTklUSU9OXG4gIC8vID09PT09PT09PT09PT09PT09PT09PT09PT09XG5cbiAgZnVuY3Rpb24gUGx1Z2luKG9wdGlvbikge1xuICAgIHJldHVybiB0aGlzLmVhY2goZnVuY3Rpb24gKCkge1xuICAgICAgdmFyICR0aGlzID0gJCh0aGlzKVxuICAgICAgdmFyIGRhdGEgID0gJHRoaXMuZGF0YSgnYnMuZHJvcGRvd24nKVxuXG4gICAgICBpZiAoIWRhdGEpICR0aGlzLmRhdGEoJ2JzLmRyb3Bkb3duJywgKGRhdGEgPSBuZXcgRHJvcGRvd24odGhpcykpKVxuICAgICAgaWYgKHR5cGVvZiBvcHRpb24gPT0gJ3N0cmluZycpIGRhdGFbb3B0aW9uXS5jYWxsKCR0aGlzKVxuICAgIH0pXG4gIH1cblxuICB2YXIgb2xkID0gJC5mbi5kcm9wZG93blxuXG4gICQuZm4uZHJvcGRvd24gICAgICAgICAgICAgPSBQbHVnaW5cbiAgJC5mbi5kcm9wZG93bi5Db25zdHJ1Y3RvciA9IERyb3Bkb3duXG5cblxuICAvLyBEUk9QRE9XTiBOTyBDT05GTElDVFxuICAvLyA9PT09PT09PT09PT09PT09PT09PVxuXG4gICQuZm4uZHJvcGRvd24ubm9Db25mbGljdCA9IGZ1bmN0aW9uICgpIHtcbiAgICAkLmZuLmRyb3Bkb3duID0gb2xkXG4gICAgcmV0dXJuIHRoaXNcbiAgfVxuXG5cbiAgLy8gQVBQTFkgVE8gU1RBTkRBUkQgRFJPUERPV04gRUxFTUVOVFNcbiAgLy8gPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT1cblxuICAkKGRvY3VtZW50KVxuICAgIC5vbignY2xpY2snLCBjbGVhck1lbnVzKVxuICAgIC5vbignY2xpY2snLCAnLmRyb3Bkb3duIGZvcm0nLCBmdW5jdGlvbiAoZSkgeyBlLnN0b3BQcm9wYWdhdGlvbigpIH0pXG4gICAgLm9uKCdjbGljaycsIHRvZ2dsZSwgRHJvcGRvd24ucHJvdG90eXBlLnRvZ2dsZSlcbiAgICAub24oJ2tleWRvd24nLCB0b2dnbGUsIERyb3Bkb3duLnByb3RvdHlwZS5rZXlkb3duKVxuICAgIC5vbigna2V5ZG93bicsICcuZHJvcGRvd24tbWVudScsIERyb3Bkb3duLnByb3RvdHlwZS5rZXlkb3duKVxuXG59KGpRdWVyeSk7XG4iXX0=
