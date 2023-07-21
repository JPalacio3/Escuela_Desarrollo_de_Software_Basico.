const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const TerserPlugin = require("terser-webpack-plugin");
const CssMinimizerPlugin = require("css-minimizer-webpack-plugin");

module.exports = {
    mode: 'production',

    output: {
        clean: true,
        filename: 'main.[contenthash].js',
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
            {
                test: /\.m?js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: [ '@babel/preset-env' ]
                    },
                },
            },
        ],
    },

    optimization: {
        minimize: true,
        minimizer: [
            new CssMinimizerPlugin(),
            new TerserPlugin(),
            new TerserPlugin(),
            new CssMinimizerPlugin(),
        ],
    },

    plugins: [
        new HtmlWebpackPlugin({
            template: 'src/index.html',
            title: 'Mi WebPack App',
            filename: 'index.html',
        }),
        new MiniCssExtractPlugin({
            filename: '[name].[fullhash].css',
        }),
    ]
};
