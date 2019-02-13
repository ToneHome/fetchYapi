/**
 * [正则表达式]
 * @type {Object}
 */
export default {
  /**
   * [email 邮箱]
   * @type {RegExp}
   * http://emailregex.com/
   */
  email: /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
  /**
   * [cellphone 手机号码]
   * @type {RegExp}
   * 移动号码段:139、138、137、136、135、134、159、158、157、150、151、152、147（数据卡）、188、187、182、183、184、178、198
   * 联通号码段:130、131、132、146、156、155、166、186、185、145（数据卡）、176
   * 电信号码段:133、153、189、180、181、177、173、199、174、141
   */
  cellphone: /^1[3-9]\d{9}$/,
  /**
   * [telephone 固定号码 格式不明？]
   * @type {RegExp}
   */
  telephone: /^(0\\d{2}-\\d{8}(-\\d{1,4})?)|(0\\d{3}-\\d{7,8}(-\\d{1,4})?)$/,
  /**
   * [chinese 汉字]
   * @type {RegExp}
   */
  chinese: /^[\u4e00-\u9fa5]*$/,
  /**
   * [charnum 英文和数字]
   * @type {RegExp}
   */
  letternum: /^[A-Za-z0-9]+$/,
  /**
   * [char2_30 长度为3-20的所有字符]
   * @type {RegExp}
   */
  char2_30: /^[^]{3,20}$/,
  /**
   * [char  由26个英文字母组成的字符串]
   * @type {RegExp}
   */
  char: /^[A-Za-z]+$/,
  /**
   * [char  ]
   * @type {RegExp}
   */
  char: /^[A-Za-z]+$/,
  /**
   * [hex  十六进制]
   * @type {RegExp}
   */
  hex: /^#?([a-f0-9]{6}|[a-f0-9]{3})$/i
};