import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

class Wk {
	static void line(String csv) {// カンマ区切りの1行を
		List < HashMap<String,String> > wk = new ArrayList< HashMap<String,String> >();// 作業テーブルを定義する
		for (String c: csv.split(",")) {
			HashMap<String,String> entity = new HashMap<>();
			entity.put("a","aa");["a","b","c"]
			entity.put("b",c);
			entity.put("c","cc");
			wk.add(entity);
		}
		for (HashMap<String,String> e:wk) {
			System.out.println(e.get("b"));
		}
		
	}
	public static void main(String[] args) {
		String file = "123,456,789\n1,2,3";
		for (String csv:file.split("\n")) {
			System.out.println(csv + "を処理します");
			line(csv);
		}
	}
}
