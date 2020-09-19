const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin');
const EncodingPlugin = require('webpack-encoding-plugin');
const VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    entry: "./Src/index.ts",
    output: {
        path: path.resolve(__dirname,"dist"),
        filename: "bundle.js"
    },
    devServer: {
        contentBase: "./dist"
    },
    plugins: [
        new HtmlWebpackPlugin({
           filename: 'index.html',
           template: './index.html' 
        }),
        new VueLoaderPlugin({

        }),
        new EncodingPlugin({
            encoding: 'iso-8859-1'
        })
    ],
    module: {
        rules: [
            {
                test: /\.vue$/,
                exclude: /node_modules/,
                use: {
                    loader: 'vue-loader'
                }
            },
            {
                test: /\.(js|ts|tsx)$/, //using regex to tell babel exactly what files to transcompile
                exclude: /node_modules/, // files to be ignored
                use: {
                    loader: 'babel-loader' // specify the loader
                } 
            }
        ]
    },
    resolve: {
        extensions: ['.js','.tsx','.ts']
    }
}