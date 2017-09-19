<template>
  <div id="app">
    <div class="container is-fluid">
      <div class="columns is-mobile">
        <div class="column">
          <div class="content-wrapper">
            <div class="field">
              <label class="label" for="search">Font Awesome Icon Finder
              </label>
              <p class="control has-icons-left has-icons-right">
                <input name="search" class="input" type="text" v-model="query" v-on:keyup="search">
                <span class="icon is-small is-left">
                  <i class="fa fa-search"></i>
                </span>
              </p>
            </div>
            <div v-if="icons.length > 0">
              <label><small>Results({{ icons.length }})</small> <small class="is-pulled-right"><i>Click on icons to copy code to clipboard</i></small></label>
              <div v-for="icon in icons">
                <div class="card">
                  <header class="card-header">
                    <p class="card-header-title">
                      {{ icon.name }}
                    </p>
                    <span class="card-header-icon has-text-grey-light" aria-label="more options">
                      <small class="tag is-light">{{ icon.categories }}</small><small class="tag is-light">{{ icon.version }}</small>
                    </span>
                  </header>
                  <div class="card-content">
                    <div class="content">
                      <div class="columns is-mobile">
                        <div class="column vc h5em">
                          <i v-clipboard:copy="getCopyText('html',icon, 5)"
                             v-clipboard:success="onCopy"
                             :class="'pointer fa fa-5x '+icon.class">
                          </i>
                        </div>
                        <div class="column vc h5em">
                          <i v-clipboard:copy="getCopyText('html',icon, 4)"
                          v-clipboard:success="onCopy"
                          :class="'pointer fa fa-4x '+icon.class"></i>
                        </div>
                        <div class="column vc h5em">
                          <i v-clipboard:copy="getCopyText('html',icon, 3)"
                          v-clipboard:success="onCopy"
                          :class="'pointer fa fa-3x '+icon.class"></i>
                        </div>
                        <div class="column vc h5em">
                          <i v-clipboard:copy="getCopyText('html',icon, 2)"
                          v-clipboard:success="onCopy"
                          :class="'pointer fa fa-2x '+icon.class"></i>
                        </div>
                        <div class="column vc h5em">
                          <i v-clipboard:copy="getCopyText('html',icon, 1)"
                          v-clipboard:success="onCopy"
                          :class="'pointer fa '+icon.class"></i>
                        </div>
                      </div>
                    </div>
                  </div>
                  <footer class="card-footer">
                    <div class="card-footer-item pointer">
                      <span v-clipboard:copy="getCopyText('square-o',icon, 0)" v-clipboard:success="onCopy" class="fa-stack fa-lg">
                        <i class="fa fa-square-o fa-stack-2x"></i>
                        <i :class="'fa '+icon.class+' fa-stack-1x'"></i>
                      </span>
                    </div>
                    <span class="card-footer-item pointer">
                      <span v-clipboard:copy="getCopyText('circle',icon, 0)" v-clipboard:success="onCopy" class="fa-stack fa-lg">
                        <i class="fa fa-circle fa-stack-2x"></i>
                        <i :class="'fa '+icon.class+' fa-stack-1x fa-inverse'"></i>
                      </span>
                    </span>
                    <span v-clipboard:copy="getCopyText('square',icon, 0)" v-clipboard:success="onCopy" class="card-footer-item pointer">
                      <span class="fa-stack fa-lg">
                        <i class="fa fa-square fa-stack-2x"></i>
                        <i :class="'fa '+icon.class+' fa-stack-1x fa-inverse'"></i>
                      </span>
                    </span>
                    <span v-clipboard:copy="getCopyText('ban',icon, 0)" v-clipboard:success="onCopy" class="card-footer-item pointer">
                      <span class="fa-stack fa-lg">
                        <i :class="'fa '+icon.class+' fa-stack-1x'"></i>
                        <i class="fa fa-ban fa-stack-2x has-text-danger"></i>
                      </span>
                    </span>
                    <a v-clipboard:copy="getCopyText('unicode', icon, 0)" v-clipboard:success="onCopy" class="card-footer-item"><small class="has-text-grey-light">[{{icon.unicode}}]</small></a>
                  </footer>
                </div>
              </div>
            </div>
            <div v-else>
              <hr>
              No results
              <br><br>
              <div class="card">
                <header class="card-header">
                  <p class="card-header-title">
                    Get started
                  </p>
                  <a href="#" class="card-header-icon" aria-label="more options">
                    <span class="icon">
                      <i class="fa fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </a>
                </header>
                <div class="card-content">
                  <div class="content">
                    <b>Font Awesome CDN</b><br>
                    Font Awesome CDN is the easiest way to get Font Awesome on your website or app, all with just a single line of code. No downloading or installing!
                    <ol>
                      <li>Copy your code & place near the top of your HTML's <code>&lt;head&gt;</code></li>
                      <li>CDN link:<pre><code class="html"><span class="nt">&lt;script</span><span class="na"> src=</span><span class="s">"https://use.fontawesome.com/452826394c.js"</span><span>&gt;</span><span class="nt">&lt;script&gt;</span>
                        </code></pre>
                      </li>
                    </ol>
                    <b>Download & Customize</b><br>
                    <ol>
                      <li>Copy the entire <code>font-awesome</code> directory into your project.</li>
                      <li>
                        In the <code>&lt;head&gt;</code> of your html, reference the location to your font-awesome.min.css.
                        <pre><code class="html"><span class="nt">&lt;link</span> <span class="na">rel=</span><span class="s">"stylesheet"</span> <span class="na">href=</span><span class="s">"path/to/font-awesome/css/font-awesome.min.css"</span><span class="nt">&gt;</span>
                        </code></pre>
                      </li>
                    </ol>
                    <a href="http://fontawesome.io/assets/font-awesome-4.7.0.zip"><i class="fa fa-download"></i>  Download Now</a>
                  </div>
                </div>
                <!-- <footer class="card-footer">
                  <a href="#" class="card-footer-item">Save</a>
                  <a href="#" class="card-footer-item">Edit</a>
                  <a href="#" class="card-footer-item">Delete</a>
                </footer> -->
              </div>
            </div>
            <div v-if="isVisible" class="overlay vc">
              <p><i class="fa fa-lg fa-clipboard"></i> Copied to clipboard!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import algoliasearch from 'algoliasearch/lite';

export default {
  name: 'app',
  data () {
    return {
      query : "",
      client: null,
      index: null,
      icons: [],
      isVisible: false
    }
  },
  mounted: function () {
    this.client = algoliasearch("*********", "*****************");
    this.index = this.client.initIndex('font_awesome');
  },
  methods: {
    search: function(){
      var that = this;
      this.index.search({ query: this.query, hitsPerPage: 1000 }, function searchDone(err, content) {
        if (err) {
          console.error(err);
          return;
        }
        if (that.query == ''){
          that.icons = []
        }else{
          that.icons = content.hits
        }
      });
    },
    onCopy: function (e) {
      this.isVisible = true;
      var that = this;
      setTimeout(function() {
        that.isVisible = false;
      }, 3000);
    },
    onError: function (e) {
      alert('Failed to copy texts')
    },
    getCopyText: function(type, icon, size){
      if (type == 'html'){
        if (size <= 1){
          return '<i class="fa fa-lg '+icon.class+'"></i>'
        }else{
          return '<i class="fa fa-'+size+'x '+icon.class+'"></i>'
        }
      }else if(type == 'square-o'){
        return '<span class="fa-stack fa-lg"><i class="fa fa-square-o fa-stack-2x"></i><i class="fa '+icon.class+' fa-stack-1x"></i></span>';
      }else if(type == 'circle'){
        return '<span class="fa-stack fa-lg"><i class="fa fa-circle fa-stack-2x"></i><i class="fa '+icon.class+' fa-stack-1x fa-inverse"></i></span>';
      }else if(type == 'square'){
        return '<span class="fa-stack fa-lg"><i class="fa fa-square fa-stack-2x"></i><i class="fa '+icon.class+' fa-stack-1x fa-inverse"></i></span>';
      }else if(type == 'ban'){
        return '<span class="fa-stack fa-lg"><i class="fa '+icon.class+' fa-stack-1x"></i><i class="fa fa-ban fa-stack-2x has-text-danger"></i></span>';
      }else{
        return icon.unicode;
      }
    }

  }
}
</script>

<style>
</style>
