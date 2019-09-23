SDK 自动发布

{{- define "name" }}
{{- if (eq .ChangeLevel "api") }}`{{ .Api }}`
{{- else if (eq .ChangeLevel "model") }}model `{{ .Model }}` at `{{ .Api }}`
{{- else if (eq .ChangeLevel "field") }}field `{{ .Field }}` at `{{ .Api }}`
{{- end }}
{{- end }}

FEATURE:
{{ range $changelog := .ChangeLogs }}
{{- if and (ne .ChangeLevel "field") }}
- {{ .ChangeType | title }} {{ template "name" . -}}
{{- end -}}
{{ end }}

ENHANCEMENT:
{{ range $changelog := .ChangeLogs }}
{{- if (eq .ChangeLevel "field") }}
- {{ if .IsCritical }}(**BREAK CHANGE**) {{ end }}{{ .ChangeType | title }} {{ template "name" . -}}
{{- end -}}
{{ end }}
