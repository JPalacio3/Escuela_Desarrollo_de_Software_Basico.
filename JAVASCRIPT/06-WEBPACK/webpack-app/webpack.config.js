const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

module.exports = {
    mode: 'development',

    output: {
        clean: true,
    },
    module: {
        rules: [
            {
                test: /\.html$/i,
                loader: 'html-loader',
                options: {
                    sources: false,
                }
            },
            {
                test: /\.css$/i,
                exclude: /main.css$/i,
                use: [ "style-loader","css-loader" ],
            },
            {
                test: /main.css$/i,
                use: [ MiniCssExtractPlugin.loader,"css-loader" ],
            },
            {
                test: /\.(png|jpe?g|gif|svg)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'img/[hash][ext][query]',
                },
            },
        ],
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: 'src/index.html',
            title: 'Mi WebPack App',
            filename: 'index.html',
        }),
        new MiniCssExtractPlugin({
            filename: 'main.css',
        }),
    ]

};
