{% load i18n djaloha_utils %}

(function (window, undefined) {
	var Aloha = window.Aloha || ( window.Aloha = {} );
	Aloha.settings = {
        {%if config.jquery_no_conflict %}
        jQuery: $.noConflict(),
        {%endif%}
        logLevels: { 'error': true, 'warn': true, 'info': true, 'debug': false, 'deprecated': true },
		errorhandling: false,
		ribbon: false,
		locale: "{%if LANGUAGE_CODE|length > 2%}{{LANGUAGE_CODE|slice:':2'}}{%else%}{{LANGAGE_CODE}}{%endif%}",
		floatingmenu: {
			"behaviour" : "float"
		},
        repositories: {
            linklist: {
		    	data: [{% for link in links %}
                    { name: "{{link.title|convert_crlf}}", url: '{{link.get_absolute_url}}', type: 'website', weight: 0.50 }{%if not forloop.last %},{%endif%}
                {% endfor %}]
			}
		},
		plugins: {
			format: {
				// all elements with no specific configuration get this configuration
				config: [  'b', 'i', 'u', 'del', 'p', 'sub', 'sup', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'pre', 'code', 'removeFormat' ],
                editables: {
					// no formatting allowed for title
					'#top-text': []
				}
			},
			list: {
				// all elements with no specific configuration get an UL, just for fun :)
				config: [ 'ul', 'ol' ],
				editables: {
					// Even if this is configured it is not set because OL and UL are not allowed in H1.
					'#top-text': []
				}
			},
			listenforcer: {
				editables: [ '.aloha-enforce-lists' ]
			},
			abbr: {
				// all elements with no specific configuration get an UL, just for fun :)
				config: [ 'abbr' ],
				editables: {
					// Even if this is configured it is not set because OL and UL are not allowed in H1.
					'#top-text': []
				}
			},
			link: {
				// all elements with no specific configuration may insert links
				config: [ 'a' ],
				editables: {
					// No links in the title.
					'#top-text': []
				},
				// all links that match the targetregex will get set the target
                // e.g. ^(?!.*aloha-editor.com).* matches all href except aloha-editor.com
				targetregex : '^http.*',
				// this target is set when either targetregex matches or not set
				// e.g. _blank opens all links in new window
				target: '_blank',
				// the same for css class as for target
				//cssclassregex: '^(?!.*aloha-editor.com).*',
				//cssclass: 'djaloha-editable',
				// use all resources of type website for autosuggest
				objectTypeFilter: ['page', 'website']
				/* handle change of href
				onHrefChange: function ( obj, href, item ) {
					var jQuery = Aloha.require( 'aloha/jquery' );
					if ( item ) {
						jQuery( obj ).attr( 'data-name', item.name );
					} else {
						jQuery( obj ).removeAttr( 'data-name' );
					}
				}*/
			},
			table: {
				// all elements with no specific configuration are not allowed to insert tables
				config: [ 'table' ],
				editables: {
					// Don't allow tables in top-text
					'#top-text': [ '' ]
				},
				summaryinsidebar: true,
					// [{name:'green', text:'Green', tooltip:'Green is cool', iconClass:'GENTICS_table GENTICS_button_green', cssClass:'green'}]
				tableConfig: [
					{ name: 'hor-minimalist-a' },
					{ name: 'box-table-a' },
					{ name: 'hor-zebra' },
				],
				columnConfig: [
					{ name: 'table-style-bigbold',  iconClass: 'aloha-button-col-bigbold' },
					{ name: 'table-style-redwhite', iconClass: 'aloha-button-col-redwhite' }
				],
				rowConfig: [
					{ name: 'table-style-bigbold',  iconClass: 'aloha-button-row-bigbold' },
					{ name: 'table-style-redwhite', iconClass: 'aloha-button-row-redwhite' }
				]
			},
            image: {
				'fixedAspectRatio' : false,
				'maxWidth'         : 600,
				'minWidth'         : 20,
				'maxHeight'        : 600,
				'minHeight'        : 20,
				'globalselector'   : '.global',
				'ui': {
					'oneTab' : false,
				}
			},
			cite: {
				referenceContainer: '#references'
			},
			formatlesspaste: {
				config: {
					button: true, // if set to false the button will be hidden
					formatlessPasteOption: true, // default state of the button
					strippedElements: [ // elements to be stripped from the pasted code
						"span",
                  		"font",
                  		"style",
						"em",
						"strong",
						"small",
						"s",
						"cite",
						"q",
						"dfn",
						"abbr",
						"time",
						"code",
						"var",
						"samp",
						"kbd",
						"sub",
						"sup",
						"i",
						"b",
						"u",
						"mark",
						"ruby",
						"rt",
						"rp",
						"bdi",
						"bdo",
						"ins",
						"del"
					]
				}
			}
		}
	};
    {%if config.jquery_no_conflict %}
    jQuery = $;
    {%endif%}

})(window);

