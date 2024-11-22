const gulp = require("gulp");
const sass = require("gulp-sass")(require("sass")); // Dart Sass
const sourcemaps = require("gulp-sourcemaps");
const uglify = require("gulp-uglify");
const babel = require("gulp-babel");

// Paths to SCSS and JS files
const paths = {
  scss: "./souled/soul/static/scss/**/*.scss", // SCSS source files
  css: "./souled/soul/static/css/", // Compiled CSS output
  js: "./souled/soul/static/js/**/*.js", // JavaScript source files
  jsDist: "./souled/soul/static/jsDist/", // Transpiled and minified JS output
};

// Compile SCSS to CSS
function compileSass() {
  return gulp
    .src(paths.scss)
    .pipe(sourcemaps.init())
    .pipe(sass({ outputStyle: "compressed" }).on("error", sass.logError))
    .pipe(sourcemaps.write("./maps"))
    .pipe(gulp.dest(paths.css));
}

// Transpile and Minify JavaScript
function processJs() {
  return gulp
    .src(paths.js)
    .pipe(sourcemaps.init())
    .pipe(
      babel({
        presets: ["@babel/preset-env"], // Transpile ES6+ to ES5
      })
    )
    .pipe(uglify()) // Minify JavaScript
    .pipe(sourcemaps.write("./maps"))
    .pipe(gulp.dest(paths.jsDist));
}

// Watch SCSS and JS files for changes
function watchFiles() {
  gulp.watch(paths.scss, compileSass); // Watch SCSS changes
  gulp.watch(paths.js, processJs); // Watch JS changes
}

// Default task
exports.default = gulp.series(
  gulp.parallel(compileSass, processJs),
  watchFiles
);
