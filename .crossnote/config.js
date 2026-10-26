({
  katexConfig: {
    "macros": {}
  },

  mathjaxConfig: {
    loader: {
      load: ['[tex]/cancel', '[tex]/enclose', '[custom]/xypic.js'],
      paths: { custom: 'https://cdn.jsdelivr.net/gh/sonoisa/XyJax-v3@3.0.1/build/' }
    },
    tex: {
      packages: { '[+]': ['cancel', 'enclose', 'xypic'] },
      //inlineMath: { '[+]': [['$', '$'], ['\\(', '\\)']] },
      //displayMath: { '[+]': [['$$', '$$'], ['\\[', '\\]']] },
      // processEscapes: false,
      //processEnvironments: true,
      //processRefs: true,
      //digits: /^(?:[0-9]+(?:\{,\}[0-9]{3})*(?:\.[0-9]*)?|\.[0-9]+)/,
      tagSide: 'right',
      tagIndent: "-10rem",
      //tagAlign: 'baseline',
      macros: {
        zerov: "{\\boldsymbol 0}",
        onev: "{\\boldsymbol 1}",
        av: "{\\boldsymbol a}",
        bv: "{\\boldsymbol b}",
        cv: "{\\boldsymbol c}",
        dv: "{\\boldsymbol d}",
        ev: "{\\boldsymbol e}",
        fv: "{\\boldsymbol f}",
        gv: "{\\boldsymbol g}",
        hv: "{\\boldsymbol h}",
        iv: "{\\boldsymbol i}",
        jv: "{\\boldsymbol j}",
        kv: "{\\boldsymbol k}",
        lv: "{\\boldsymbol l}",
        mv: "{\\boldsymbol m}",
        nv: "{\\boldsymbol n}",
        ov: "{\\boldsymbol o}",
        pv: "{\\boldsymbol p}",
        qv: "{\\boldsymbol q}",
        rv: "{\\boldsymbol r}",
        sv: "{\\boldsymbol s}",
        tv: "{\\boldsymbol t}",
        uv: "{\\boldsymbol u}",
        vv: "{\\boldsymbol v}",
        wv: "{\\boldsymbol w}",
        xv: "{\\boldsymbol x}",
        yv: "{\\boldsymbol y}",
        zv: "{\\boldsymbol z}",
        Av: "{\\mathbf A}",
        Bv: "{\\mathbf B}",
        Cv: "{\\mathbf C}",
        Dv: "{\\mathbf D}",
        Ev: "{\\mathbf E}",
        Fv: "{\\mathbf F}",
        Gv: "{\\mathbf G}",
        Hv: "{\\mathbf H}",
        Iv: "{\\mathbf I}",
        Jv: "{\\mathbf J}",
        Kv: "{\\mathbf K}",
        Lv: "{\\mathbf L}",
        Mv: "{\\mathbf M}",
        Nv: "{\\mathbf N}",
        Ov: "{\\mathbf O}",
        Pv: "{\\mathbf P}",
        Qv: "{\\mathbf Q}",
        Rv: "{\\mathbf R}",
        Sv: "{\\mathbf S}",
        Tv: "{\\mathbf T}",
        Uv: "{\\mathbf U}",
        Vv: "{\\mathbf V}",
        Wv: "{\\mathbf W}",
        Xv: "{\\mathbf X}",
        Yv: "{\\mathbf Y}",
        Zv: "{\\mathbf Z}",
        alphav: "{\\boldsymbol {\\alpha}}",
        betav: "{\\boldsymbol {\\beta}}",
        lambdav: "{\\boldsymbol {\\lambda}}",
        muv: "{\\boldsymbol {\\mu}}",
        thetav: "{\\boldsymbol {\\theta}}",
        phiv: "{\\boldsymbol {\\phi}}",
        epsilonv: "{\\boldsymbol {\\epsilon}}",
        varphiv: "{\\boldsymbol {\\varphi}}",
        zetav: "{\\boldsymbol {\\zeta}}",
        deltav: "{\\boldsymbol {\\delta}}",
        sigmav: "{\\boldsymbol {\\sigma}}",
        Sigmav: "{\\boldsymbol {\\Sigma}}",
        Phiv: "{\\boldsymbol {\\Phi}}",
        Lambdav: "{\\boldsymbol {\\Lambda}}",
        Omegav: "{\\boldsymbol {\\Omega}}",
        cb: "{\\mathbb C}",
        eb: "{\\mathbb E}",
        fb: "{\\mathbb F}",
        hb: "{\\mathbb H}",
        ib: "{\\mathbb I}",
        nb: "{\\mathbb N}",
        pb: "{\\mathbb P}",
        qb: "{\\mathbb Q}",
        rb: "{\\mathbb R}",
        vb: "{\\mathbb V}",
        zb: "{\\mathbb Z}",
        ac: "{\\mathcal A}",
        bc: "{\\mathcal B}",
        cc: "{\\mathcal C}",
        dc: "{\\mathcal D}",
        ec: "{\\mathcal E}",
        fc: "{\\mathcal F}",
        gc: "{\\mathcal G}",
        hc: "{\\mathcal H}",
        ic: "{\\mathcal I}",
        jc: "{\\mathcal J}",
        kc: "{\\mathcal K}",
        lc: "{\\mathcal L}",
        mc: "{\\mathcal M}",
        nc: "{\\mathcal N}",
        oc: "{\\mathcal o}",
        pc: "{\\mathcal P}",
        qc: "{\\mathcal Q}",
        rc: "{\\mathcal R}",
        sc: "{\\mathcal S}",
        tc: "{\\mathcal T}",
        uc: "{\\mathcal U}",
        vc: "{\\mathcal V}",
        wc: "{\\mathcal W}",
        xc: "{\\mathcal X}",
        yc: "{\\mathcal Y}",
        zc: "{\\mathcal Z}",
        as: "{\\mathscr A}",
        ds: "{\\mathscr D}",
        ls: "{\\mathscr L}",
        xbar: "{\\bar {x}}",
        ybar: "{\\bar {y}}",
        Bbar: "{\\bar B}",
        yvbar: "{\\bar {\\yv}}",
        fh: "{\\hat f}",
        wh: "{\\hat w}",
        xh: "{\\hat x}",
        yh: "{\\hat y}",
        xvh: "{\\hat {\\xv}}",
        yvh: "{\\hat {\\yv}}",
        Xvh: "{\\hat {\\Xv}}",
        wvt: "{\\tilde {\\wv}}",
        xvt: "{\\tilde {\\xv}}",
        yvt: "{\\tilde {\\yv}}",
        Kvt: "{\\tilde {\\Kv}}",
        Ff: "{\\mathfrak F}",

        diff: "{\\mathrm {d}}",
        diag: "{\\textrm {diag}}",
        dist: "{\\textrm {dist}}",
        // 公式中的文字
        acc: "{\\textrm {acc}}",
        err: "{\\textrm {err}}",
        mse: "{\\textrm {MSE}}",
        bias: "{\\textrm {bias}}",
        variance: "{\\textrm {variance}}",
        noise: "{\\textrm {noise}}",
        st: "{\\textrm {s.t.}}",
        VC: "{\\textrm {VC}}",
        prior: "{\\textrm {prior}}",
        posterior: "{\\textrm {posterior}}",
        erm: "{\\textrm {ERM}}",
        gru: "{\\textrm {GRU}}",
        lstm: "{\\textrm {LSTM}}",
        mode: "{\\textrm {mode}}",

        maxt: "{\\textrm {max}}",
        mint: "{\\textrm {min}}",
        median: "{\\textrm {median}}",
        span: "{\\textrm {span}}",

        TP: "{\\textrm {TP}}",
        FP: "{\\textrm {FP}}",
        TN: "{\\textrm {TN}}",
        FN: "{\\textrm {FN}}",
        SSE: "{\\textrm {SSE}}",
        SSB: "{\\textrm {SSB}}",
        gain: "{\\textrm {Gain}}",
        gini: "{\\textrm {Gini}}",

        train: "{\\textrm {train}}",
        val: "{\\textrm {validation}}",

        
        sign: "{\\mathrm {sign}}",
        sgn: "{\\mathrm {sgn}}",
        
        
        shu: "{|}",
        shuu: "{\\|}",


        Pr: "{\\mathrm {Pr}}",
        gcd: "{\\mathrm {gcd}}",

        // 激活函数
        tanh: "{\\mathrm {tanh}}",
        logistic: "{\\textrm {logistic}}",
        softmax: "{\\textrm {softmax}}",
        LL: "{\\textrm {LL}}",
        relu: "{\\textrm {ReLU}}",
        lrelu: "{\\textrm {LeakyReLU}}",
        prelu: "{\\textrm {PReLU}}",
        elu: "{\\textrm {ELU}}",
        softplus: "{\\textrm {Softplus}}",
        swish: "{\\textrm {Swish}}",
        maxout: "{\\textrm {Maxout}}",
        const: "{\\textrm {const}}",
        cov: "{\\mathrm {cov}}",
        grad: "{\\mathrm {grad}}",
        div: "{\\mathrm {div}}",
        var: "{\\mathrm {var}}",
        
        att: "{\\mathrm {att}}",
        cut: "{\\mathrm {cut}}",
        rcut: "{\\mathrm {RatioCut}}",
        ncut: "{\\mathrm {NCut}}",
        tr: "{\\mathrm {tr}}",
        true: "{\\mathrm {True}}",
        false: "{\\mathrm {False}}",
        lis: "{\\mathrm {LIS}}",
        ins: "{\\mathrm {ins}}",
        greedy: "{\\mathrm {greedy}}",
        vol: "{\\mathrm {vol}}",
        mlp: "{\\mathrm {MLP}}",
        map: "{\\mathrm {MAP}}",
        ml: "{\\mathrm {ML}}",
        update: "{\\mathrm {Update}}",
        aggregate: "{\\mathrm {Aggregate}}",
        self: "{\\mathrm {self}}",
        set: "{\\mathrm {set}}",
        neigh: "{\\mathrm {neigh}}",
        base: "{\\mathrm {base}}",
        NULL: "{\\mathrm {NULL}}",
        new: "{\\mathrm {new}}",
        
        edge: "{\\textrm {edge}}",
        node: "{\\textrm {node}}",
        graph: "{\\textrm {graph}}",
        
        dep: "{\\mathrm {dep}}",
        len: "{\\mathrm {len}}",
        dec: "{\\mathrm {Dec}}",
        sym: "{\\mathrm {sym}}",
        
        hp: "{\\mathrm {hp}}",
        gen: "{\\mathrm {gen}}",
        ow: "{\\mathrm {o.w.}}",
        // 概率分布
        Bern: "{\\textrm {Bern}}",
        BetaDist: "{\\mathrm {Beta}}",
        BetaFunc: "{\\mathrm {B}}",
        Gam: "{\\mathrm {Gam}}",
        Dir: "{\\textrm {Dir}}",
        rot: "{\\mathbf {rot180}}",
        up: "{\\mathbf {up}}",
        cen: "{\\mathrm {cen}}",
        con: "{\\mathrm {con}}",
        TG: "{\\textrm {TreeGenerate}}",
        
        argmin: "{\\mathop{\\mathrm{argmin}}}",
        argmax: "{\\mathop{\\mathrm{argmax}}}",
      },
    },
    chtml: {
      matchFontHeight: true,  // True to scale the math to match the ex-height of the surrounding font
      adaptiveCSS: true,      // true means only produce CSS that is used in the processed equations
    },
    output: { // 这些是v4才有的设置
      scale: 1,                      // global scaling factor for all expressions
      minScale: .5,                  // smallest scaling factor to use
      mtextInheritFont: false,       // true to make mtext elements use surrounding font
      merrorInheritFont: true,      // true to make merror text use surrounding font
      mtextFont: 'Ysabeau',                 // font to use for mtext, if not inheriting (empty means use MathJax fonts)
      merrorFont: 'serif',           // font to use for merror, if not inheriting (empty means use MathJax fonts)
      unknownFamily: 'LXGWSong',        // font to use for character that aren't in MathJax's fonts
      mathmlSpacing: false,          // true for MathML spacing rules, false for TeX rules
      skipAttributes: {},            // RFDa and other attributes NOT to copy to the output
      exFactor: .5,                  // default size of ex in em units
      displayAlign: 'left',        // default for indentalign when set to 'auto'
      displayIndent: '1em',            // default for indentshift when set to 'auto'
      displayOverflow: 'scroll',   // 公式过长 默认overflow (scroll/scale/truncate/elide/linebreak/overflow)
      linebreaks: {                  // options for when overflow is linebreak
        inline: true,                // true for browser-based breaking of inline equations
        width: '100%',               // a fixed size or a percentage of the container width
        lineleading: .2,             // the default lineleading in em units
      },
      font: '',                      // the font component to load
      fontPath: "",            // The path to the font definitions
      fontExtensions: [],            // The font extensions to load
      htmlHDW: 'auto',               // 'use', 'force', or 'ignore' data-mjx-hdw attributes
      preFilters: [],                // A list of pre-filters to add to the output jax
      postFilters: [],               // A list of post-filters to add to the output jax
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'annotation', 'annotation-xml'],
      includeHtmlTags: { br: '\n', wbr: '', '#comment': '' },
      ignoreHtmlClass: 'tex2jax_ignore',    //  class that marks tags not to search
      processHtmlClass: 'tex2jax_process',  //  class that marks tags that should be searched
      compileError: function (doc, math, err) { doc.compileError(math, err) },
      typesetError: function (doc, math, err) { doc.typesetError(math, err) },
      renderActions: {}
    },
  },

  mermaidConfig: {
    "startOnLoad": false
  },
})