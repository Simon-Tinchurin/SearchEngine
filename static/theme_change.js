var themeLink = document.getElementById('theme-link');
var colorModeCheckbox = document.getElementById('color_mode');

// Check if a theme is already selected in the local storage
var storedTheme = localStorage.getItem('selectedTheme');
if (storedTheme === 'dark') {
  themeLink.href = 'static/dark.css';
  colorModeCheckbox.checked = true;
}

colorModeCheckbox.addEventListener('change', function() {
  if (this.checked) {
    themeLink.href = 'static/dark.css';
    localStorage.setItem('selectedTheme', 'dark');
  } else {
    themeLink.href = 'static/light.css';
    localStorage.setItem('selectedTheme', 'light');
  }
});
