<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:output omit-xml-declaration="yes" indent="no" />

	<xsl:param name="id" />

	<xsl:template match="/LanguageData">

<!-- <xsl:value-of select="count(/LanguageData/Language/GeneralInfo/LangID)" />
 -->		
			<xsl:apply-templates select="Language" />
	</xsl:template>
	<xsl:template match="Language/GeneralInfo">
			<p>
			<xsl:value-of select="LangID" />
 			</p>
	</xsl:template>

	<!-- ignore text content of nodes -->
	<xsl:template match="text()" />

</xsl:stylesheet>