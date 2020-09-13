// const IS_PRODUCTION = process.env.NODE_ENV === 'production'
const path = require("path");

module.exports = {
  outputDir: "dist",
  assetsDir: "static",
  // baseUrl: IS_PRODUCTION
  // ? 'http://cdn123.com'
  // : '/',
  // For Production, replace set baseUrl to CDN
  // And set the CDN origin to `yourdomain.com/static`
  // Whitenoise will serve once to CDN which will then cache
  // and distribute
  devServer: {
    proxy: {
      "/api*": {
        // Forward frontend dev server request for /api to django dev server
        target: "http://127.0.0.1:8000"
      }
    },
    public: "http://127.0.0.1:8080",
    // hot and liveReload must be false to remove HMR
    // console will log "[HMR] Waiting for update signal from WDS..."
    // but WDS will not send any signal for update
    hot: true,
    liveReload: true,
  },
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "sass",
      patterns: [path.resolve(__dirname, "./src/assets/scss/template.scss")]
    }
  },
  css: {
    loaderOptions: {
      sass: {
        data: `
            @import "@/assets/scss/_base.scss";
          `
      }
    }
  },
};
