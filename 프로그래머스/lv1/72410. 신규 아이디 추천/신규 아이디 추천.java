class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        new_id = new_id.replaceAll("[^a-z0-9\\-_.]", "");
        new_id = new_id.replaceAll("\\.+", ".");
        if (!new_id.isEmpty() && new_id.charAt(0) == '.')
            new_id = new_id.substring(1);
        if (!new_id.isEmpty() && new_id.charAt(new_id.length() - 1) == '.')
            new_id = new_id.substring(0, new_id.length() - 1);
        if (new_id.isEmpty())
            new_id = "a";
        if (new_id.length() > 15)
            new_id = new_id.charAt(14) != '.' ? new_id.substring(0, 15) : new_id.substring(0, 14);
        if (new_id.length() < 3)
            new_id += Character.toString(new_id.charAt(new_id.length() - 1)).repeat(3 - new_id.length());
        
        return new_id;
    }
}